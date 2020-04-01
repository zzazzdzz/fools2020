Imports System.Net.Sockets
Imports System.Threading

Public Class BGBProto

    Dim client As TcpClient
    Dim buf(8) As Byte
    Dim outbuf(8) As Byte

    Public Shared SessionID As String

    Sub RecvPacket(ByVal stream As NetworkStream)
        Dim at = 0
        Do
            Dim numRead = stream.Read(buf, at, 8 - at)
            at += numRead
        Loop Until at = 8
    End Sub

    Enum RecvByteState As Integer
        STATE_HANDSHAKE_FIRST
        STATE_HANDSHAKE_SECOND
        STATE_HANDSHAKE_THIRD
        STATE_RECV_HEADER
        STATE_RECV_REQ
        STATE_HANDLE_REQ
        STATE_SEND_RESP
    End Enum

    Dim recvstate As RecvByteState
    Dim hdr As New Collections.Generic.List(Of Byte)
    Dim data As New Collections.Generic.List(Of Byte)
    Dim datalen As Integer = 0

    Dim respready As Integer = 0

    Sub HandleRequest()
        Dim body = System.Convert.ToBase64String(data.ToArray())
        Dim cli As New Net.WebClient
        Try
            Dim resp = cli.UploadString("http://127.0.0.1:20111/req/" & SessionID, body)
            Dim resparr = System.Convert.FromBase64String(resp)
            data.Clear()
            For Each b In resparr
                data.Add(b)
            Next
        Catch ex As Exception
            data.Clear()
            data.Add(0)
            data.Add(0)
            data.Add(1)
            data.Add(0)
            data.Add(&HFC)
            data.Add(&HFC)
            data.Add(0)
        End Try
        respready = 1
    End Sub

    Function RecvByte(ByVal b As Byte) As Byte
        Debug.WriteLine("state=" & recvstate & " b=" & Hex(b))
        If recvstate = RecvByteState.STATE_HANDSHAKE_FIRST Then
            If b = &H6D Then
                recvstate = RecvByteState.STATE_HANDSHAKE_SECOND
                Return &H3A
            Else
                recvstate = RecvByteState.STATE_HANDSHAKE_FIRST
                Return &HFF
            End If
        End If
        If recvstate = RecvByteState.STATE_HANDSHAKE_SECOND Then
            If b = &HA4 Then
                recvstate = RecvByteState.STATE_HANDSHAKE_THIRD
                Return &HF1
            Else
                recvstate = RecvByteState.STATE_HANDSHAKE_FIRST
                Return &HFF
            End If
        End If
        If recvstate = RecvByteState.STATE_HANDSHAKE_THIRD Then
            If b = &HD1 Then
                hdr.Clear()
                data.Clear()
                recvstate = RecvByteState.STATE_RECV_HEADER
                Return &H65
            Else
                recvstate = RecvByteState.STATE_HANDSHAKE_FIRST
                Return &HFF
            End If
        End If
        If recvstate = RecvByteState.STATE_RECV_HEADER Then
            hdr.Add(b)
            If hdr.Count = 6 Then
                datalen = hdr(2) + hdr(3) * 256
                For Each bb In hdr
                    data.Add(bb)
                Next
                recvstate = RecvByteState.STATE_RECV_REQ
            End If
            Return &HCD
        End If
        If recvstate = RecvByteState.STATE_RECV_REQ Then
            data.Add(b)
            datalen -= 1
            If datalen <= 0 Then
                respready = 0
                Dim th As New Thread(AddressOf HandleRequest)
                th.Start()
                recvstate = RecvByteState.STATE_HANDLE_REQ
            End If
            Return &HCC
        End If
        If recvstate = RecvByteState.STATE_HANDLE_REQ Then
            If respready = 1 Then
                datalen = 0
                recvstate = RecvByteState.STATE_SEND_RESP
                Return &HCF
            Else
                Return &HCC
            End If
        End If
        If recvstate = RecvByteState.STATE_SEND_RESP Then
            Dim d = data(datalen)
            datalen += 1
            If datalen >= data.Count Then
                recvstate = RecvByteState.STATE_HANDSHAKE_FIRST
            End If
            Return d
        End If
    End Function

    Sub SendPacket(ByVal stream As NetworkStream, ByVal cmd As Byte, ByVal a As Byte, ByVal b As Byte, ByVal c As Byte, ByVal ts As UInteger)
        outbuf(0) = cmd
        outbuf(1) = a
        outbuf(2) = b
        outbuf(3) = c
        outbuf(4) = ts And &HFF
        outbuf(5) = (ts >> 8) And &HFF
        outbuf(6) = (ts >> 16) And &HFF
        outbuf(7) = (ts >> 24) And &HFF
        stream.Write(outbuf, 0, 8)
    End Sub

    Sub HandleClientThread()
        Dim stream As NetworkStream = Me.client.GetStream()
        SendPacket(stream, 1, 1, 4, 0, 0)
        Do
            RecvPacket(stream)
            If buf(0) = 1 Then
                SendPacket(stream, 108, &H5, 0, 0, 0)
            ElseIf buf(0) = 104 Then
                'Debug.WriteLine(BitConverter.ToString(buf))
                SendPacket(stream, 105, RecvByte(buf(1)), 0, 0, 0)
            ElseIf buf(0) = 106 Then
                SendPacket(stream, 106, 0, 0, 0, 0)
            ElseIf buf(0) = 108 Then
                SendPacket(stream, 106, 0, 0, 0, 0)
            Else
                'Debug.WriteLine(BitConverter.ToString(buf))
            End If
        Loop
    End Sub

    Public Sub Start(ByVal c As TcpClient)
        Me.client = c
        Dim th As New Thread(AddressOf HandleClientThread)
        th.IsBackground = True
        th.Start()
    End Sub
End Class
