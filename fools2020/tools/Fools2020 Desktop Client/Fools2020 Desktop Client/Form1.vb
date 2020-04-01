Imports System.Net.Sockets
Imports System.Net
Imports System.Threading

Public Class Form1

    Sub ServerThread()
        Dim sock As New TcpListener(New IPAddress(&H100007F), 8765)
        sock.Start()
        Do
            Dim client As TcpClient = sock.AcceptTcpClient()
            client.NoDelay = True
            Dim r As New BGBProto()
            r.Start(client)
        Loop
    End Sub

    Private Delegate Sub ShowPanelDelegate()
    Private Sub ShowPanel()
        Panel1.Show()
    End Sub

    Sub LoginThread()
        Try
            Dim cli As New Net.WebClient
            Dim body = System.Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(TextBox1.Text)) & "|" & System.Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(TextBox2.Text))
            Dim resp = cli.UploadString("http://127.0.0.1:20111/login/", body)
            If resp = "INVAL" Then
                MsgBox("Invalid username and/or password.")
                Button1.Enabled = True
                TextBox1.Enabled = True
                TextBox2.Enabled = True
            Else
                BGBProto.SessionID = resp
                Button1.Text = "Connected!"
                Label4.Text = "Logged in as: " & TextBox1.Text
                Me.Invoke(New ShowPanelDelegate(AddressOf ShowPanel))
            End If
        Catch ex As Exception
            MsgBox("Could not connect to the server.")
            Button1.Enabled = True
            TextBox1.Enabled = True
            TextBox2.Enabled = True
        End Try
    End Sub

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim th As New Thread(AddressOf ServerThread)
        th.IsBackground = True
        th.Start()
        Control.CheckForIllegalCrossThreadCalls = False ' this is so bad
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Button1.Enabled = False
        TextBox1.Enabled = False
        TextBox2.Enabled = False
        Dim th As New Thread(AddressOf LoginThread)
        th.IsBackground = True
        th.Start()
    End Sub
End Class
