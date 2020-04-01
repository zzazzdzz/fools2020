Public Class Form1

    Const BASE_PATH As String = "W:\code\fools2020\mapsraw"
    Const TILESET_PATH As String = "W:\code\fools2018\mapeditor\tileset%"
    Dim mapdata As String = ""
    Dim targetx As Integer = 0
    Dim targety As Integer = 0

    Dim curmapindex = -1

    Dim curselblock = 0
    Dim drawmode = 0
    Dim allowblockedit = 0
    Dim borderblock = 0

    Dim connectionN As Integer = 0
    Dim connectionS As Integer = 0
    Dim connectionW As Integer = 0
    Dim connectionE As Integer = 0

    Dim connectionN_X As Integer = 0
    Dim connectionS_X As Integer = 0
    Dim connectionW_X As Integer = 0
    Dim connectionE_X As Integer = 0
    Dim connectionN_Y As Integer = 0
    Dim connectionS_Y As Integer = 0
    Dim connectionW_Y As Integer = 0
    Dim connectionE_Y As Integer = 0

    Dim prevx = 0
    Dim prevy = 0
    Dim hoverx = 0
    Dim hovery = 0

    Dim sprites() As String = {"SPRITE_BLUE", "SPRITE_OAK", "SPRITE_BUG_CATCHER", "SPRITE_SLOWBRO", "SPRITE_LASS", "SPRITE_BLACK_HAIR_BOY_1", "SPRITE_LITTLE_GIRL", "SPRITE_BIRD", "SPRITE_FAT_BALD_GUY", "SPRITE_GAMBLER", "SPRITE_BLACK_HAIR_BOY_2", "SPRITE_GIRL", "SPRITE_HIKER", "SPRITE_FOULARD_WOMAN", "SPRITE_GENTLEMAN", "SPRITE_DAISY", "SPRITE_BIKER", "SPRITE_SAILOR", "SPRITE_COOK", "SPRITE_BIKE_SHOP_GUY", "SPRITE_MR_FUJI", "SPRITE_GIOVANNI", "SPRITE_ROCKET", "SPRITE_MEDIUM", "SPRITE_WAITER", "SPRITE_ERIKA", "SPRITE_MOM_GEISHA", "SPRITE_BRUNETTE_GIRL", "SPRITE_LANCE", "SPRITE_OAK_SCIENTIST_AIDE", "SPRITE_OAK_AIDE", "SPRITE_ROCKER", "SPRITE_SWIMMER", "SPRITE_WHITE_PLAYER", "SPRITE_GYM_HELPER", "SPRITE_OLD_PERSON", "SPRITE_MART_GUY", "SPRITE_FISHER", "SPRITE_OLD_MEDIUM_WOMAN", "SPRITE_NURSE", "SPRITE_CABLE_CLUB_WOMAN", "SPRITE_MR_MASTERBALL", "SPRITE_LAPRAS_GIVER", "SPRITE_WARDEN", "SPRITE_SS_CAPTAIN", "SPRITE_FISHER2", "SPRITE_BLACKBELT", "SPRITE_GUARD", "SPRITE_COP_GUARD", "SPRITE_MOM", "SPRITE_BALDING_GUY", "SPRITE_YOUNG_BOY", "SPRITE_GAMEBOY_KID", "SPRITE_GAMEBOY_KID_COPY", "SPRITE_CLEFAIRY", "SPRITE_AGATHA", "SPRITE_BRUNO", "SPRITE_LORELEI", "SPRITE_SEEL", "SPRITE_BALL", "SPRITE_OMANYTE", "SPRITE_BOULDER", "SPRITE_PAPER_SHEET", "SPRITE_BOOK_MAP_DEX", "SPRITE_CLIPBOARD", "SPRITE_SNORLAX", "SPRITE_OLD_AMBER_COPY", "SPRITE_OLD_AMBER", "SPRITE_LYING_OLD_MAN_UNUSED_1", "SPRITE_LYING_OLD_MAN_UNUSED_2", "SPRITE_LYING_OLD_MAN"}

    Dim tilesetimages(256) As Drawing.Image

    Function hex2(ByVal s As Integer) As String
        Dim q = Hex(s)
        If q.Length < 2 Then
            q = "0" & q
        End If
        Return q
    End Function

    Function hex4(ByVal s As Integer) As String
        Dim q = Hex(s)
        While q.Length < 4
            q = "0" & q
        End While
        Return q
    End Function

    Sub writechangestofile()
        Dim fname = BASE_PATH & "\" & ListBox1.Items(curmapindex)
        Dim fpold = My.Computer.FileSystem.ReadAllText(fname)
        Dim fp = fpold.Replace(vbCrLf, vbLf).Split(vbLf)
        Dim newfp = ""
        Dim gogogo = 0
        Dim whichdb = 0
        For Each i In fp
            If i.Contains("hdr_border") Then
                newfp &= "    hdr_border          $" & hex2(borderblock) & vbCrLf
                Continue For
            End If
            If i.Contains("hdr_connection      NORTH, ") Then
                newfp &= "    hdr_connection      NORTH, $" & hex4(connectionN) & ", " & connectionN_X & ", " & connectionN_Y & vbCrLf
                Continue For
            End If
            If i.Contains("hdr_connection      SOUTH, ") Then
                newfp &= "    hdr_connection      SOUTH, $" & hex4(connectionS) & ", " & connectionS_X & ", " & connectionS_Y & vbCrLf
                Continue For
            End If
            If i.Contains("hdr_connection      WEST,  ") Then
                newfp &= "    hdr_connection      WEST,  $" & hex4(connectionW) & ", " & connectionW_X & ", " & connectionW_Y & vbCrLf
                Continue For
            End If
            If i.Contains("hdr_connection      EAST,  ") Then
                newfp &= "    hdr_connection      EAST,  $" & hex4(connectionE) & ", " & connectionE_X & ", " & connectionE_Y & vbCrLf
                Continue For
            End If
            If i.EndsWith("_Objects:") Then
                gogogo = 1
                newfp &= i & vbCrLf
                Continue For
            End If
            If gogogo = 1 Then
                If Not i.Contains("hdr_") Then
                    gogogo = 0
                    For Each ii As String In ListBox2.Items
                        newfp &= "    " & ii & vbCrLf
                    Next
                    newfp &= vbCrLf
                    Continue For
                End If
                Continue For
            End If
            If i.Contains("hdr_music") Then
                newfp &= "    hdr_music           " & ComboBox1.Items(ComboBox1.SelectedIndex) & vbCrLf
                Continue For
            End If
            If i.Contains("hdr_textptrs") Then
                newfp &= "    hdr_textptrs        " & TextBox5.Text.Replace(" ", "") & vbCrLf
                Continue For
            End If
            If i.Contains("hdr_palette") Then
                newfp &= "    hdr_palette         " & ComboBox2.Items(ComboBox2.SelectedIndex).ToString().Substring(0, 3) & vbCrLf
                Continue For
            End If
            If i.Contains("db ") Then
                newfp &= "    db " & mapdata.Split(vbLf)(whichdb) & vbCrLf
                whichdb += 1
                Continue For
            End If
            newfp &= i & vbCrLf
        Next
        If Not My.Computer.FileSystem.FileExists(fname & ".bak") Then
            My.Computer.FileSystem.WriteAllText(fname & ".bak", fpold, False, System.Text.Encoding.ASCII)
        End If
        My.Computer.FileSystem.WriteAllText(fname, newfp, False, System.Text.Encoding.ASCII)
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        lastconn = 0
        curmapindex = ListBox1.SelectedIndex
        If curmapindex = -1 Then
            Return
        End If
        Dim fp = My.Computer.FileSystem.ReadAllText(BASE_PATH & "\" & ListBox1.Items(ListBox1.SelectedIndex)).Replace(vbCrLf, vbLf).Split(vbLf)
        Dim gogogo = 0
        mapdata = ""
        ListBox2.Items.Clear()
        For Each i In fp
            If i.Contains("hdr_connection      NORTH, ") Then
                connectionN = CInt("&H" & i.Replace("    hdr_connection      NORTH, $", "").Substring(0, 4))
                connectionN_X = CInt(i.Split(",")(2))
                connectionN_Y = CInt(i.Split(",")(3))
            End If
            If i.Contains("hdr_connection      SOUTH, ") Then
                connectionS = CInt("&H" & i.Replace("    hdr_connection      SOUTH, $", "").Substring(0, 4))
                connectionS_X = CInt(i.Split(",")(2))
                connectionS_Y = CInt(i.Split(",")(3))
            End If
            If i.Contains("hdr_connection      WEST,  ") Then
                connectionW = CInt("&H" & i.Replace("    hdr_connection      WEST,  $", "").Substring(0, 4))
                connectionW_X = CInt(i.Split(",")(2))
                connectionW_Y = CInt(i.Split(",")(3))
            End If
            If i.Contains("hdr_connection      EAST,  ") Then
                connectionE = CInt("&H" & i.Replace("    hdr_connection      EAST,  $", "").Substring(0, 4))
                connectionE_X = CInt(i.Split(",")(2))
                connectionE_Y = CInt(i.Split(",")(3))
            End If
            If i.EndsWith("_Blocks:") Then
                gogogo = 1
                Continue For
            End If
            If gogogo = 1 Then
                If Not i.Contains("db") Then
                    gogogo = 0
                    If mapdata.EndsWith(vbLf) Then
                        mapdata = mapdata.Substring(0, Len(mapdata) - 1)
                    End If
                    Continue For
                End If
                mapdata &= i.Replace("    db ", "") & vbLf
            End If
            If i.Contains("hdr_sign") Or i.Contains("hdr_object") Or i.Contains("hdr_warp") Then
                ListBox2.Items.Add(i.Trim())
            End If
            If i.Contains("hdr_tileset") Then
                loadtileset(CInt(i.Split(" ").Last()))
            End If
            If i.Contains("hdr_border") Then
                borderblock = (CInt("&H" & i.Split(" ").Last().Replace("$", "")))
                TextBox4.Text = borderblock
            End If
            If i.Contains("hdr_textptrs") Then
                TextBox5.Text = (i.Split(" ").Last())
            End If
            If i.Contains("hdr_music") Then
                ComboBox1.SelectedIndex = 0
                For q As Integer = 0 To ComboBox1.Items.Count - 1
                    If ComboBox1.Items(q).ToString().Contains(i.Replace("    hdr_music           ", "")) Then
                        ComboBox1.SelectedIndex = q
                    End If
                Next
            End If
            If i.Contains("hdr_palette") Then
                ComboBox2.SelectedIndex = 0
                For q As Integer = 0 To ComboBox2.Items.Count - 1
                    If ComboBox2.Items(q).ToString().Contains(i.Replace("    hdr_palette         ", "").ToUpper()) Then
                        ComboBox2.SelectedIndex = q
                    End If
                Next
            End If
        Next
        ' MsgBox(connectionN & "," & connectionS & "," & connectionW & "," & connectionE)
        Panel1.Invalidate()
    End Sub

    Private Sub Panel1_Paint(ByVal sender As System.Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Panel1.Paint
        If ListBox1.SelectedIndex = -1 Then
            Exit Sub
        End If
        Dim g As Graphics = e.Graphics
        Dim md = mapdata.Split(vbLf)
        Dim y = 0
        For Each i In md
            If i.Length < 3 Then
                Continue For
            End If
            Dim isplit = i.Split(",")
            Dim x = 0
            For Each q In isplit
                g.DrawImage(tilesetimages(CInt("&H" & q.Replace("$", ""))), x * 32, y * 32, 32, 32)
                x += 1
            Next
            y += 1
        Next
        g.DrawRectangle(Pens.Red, New Rectangle(targetx * 16, targety * 16, 16, 16))
        g.DrawRectangle(Pens.Blue, New Rectangle(hoverx * 16, hovery * 16, 16, 16))
        Try
            For Each i As String In ListBox2.Items
                If i.StartsWith("hdr_object ") Then
                    Dim origi = i
                    Dim gx = CInt(i.Split(",")(1))
                    Dim gy = CInt(i.Split(",")(2))
                    g.DrawRectangle(New Pen(Color.Black, 2), New Rectangle(gx * 16, gy * 16, 16, 16))
                    If ListBox2.SelectedIndex <> -1 Then
                        If ListBox2.Items(ListBox2.SelectedIndex) = origi Then
                            g.DrawRectangle(New Pen(Color.Red, 2), New Rectangle(gx * 16 - 3, gy * 16 - 3, 24 - 2, 24 - 2))
                        End If
                    End If
                End If
                If i.StartsWith("hdr_signpost ") Then
                    Dim origi = i
                    i = i.Replace("hdr_signpost        ", "")
                    Dim gx = CInt(i.Split(",")(0))
                    Dim gy = CInt(i.Split(",")(1))
                    g.DrawRectangle(New Pen(Color.Green, 2), New Rectangle(gx * 16, gy * 16, 16, 16))
                    If ListBox2.SelectedIndex <> -1 Then
                        If ListBox2.Items(ListBox2.SelectedIndex) = origi Then
                            g.DrawRectangle(New Pen(Color.Red, 2), New Rectangle(gx * 16 - 3, gy * 16 - 3, 24 - 2, 24 - 2))
                        End If
                    End If
                End If
                If i.StartsWith("hdr_warp ") Then
                    Dim origi = i
                    i = i.Replace("hdr_warp            ", "")
                    Dim gx = CInt(i.Split(",")(0))
                    Dim gy = CInt(i.Split(",")(1))
                    g.DrawRectangle(New Pen(Color.Purple, 2), New Rectangle(gx * 16, gy * 16, 16, 16))
                    If ListBox2.SelectedIndex <> -1 Then
                        If ListBox2.Items(ListBox2.SelectedIndex) = origi Then
                            g.DrawRectangle(New Pen(Color.Red, 2), New Rectangle(gx * 16 - 3, gy * 16 - 3, 24 - 2, 24 - 2))
                        End If
                    End If
                End If
            Next
        Catch ex As Exception
            g.DrawString("Error in events", New Drawing.Font("Courier New", 20, FontStyle.Bold), Brushes.Red, 5, 5)
        End Try
    End Sub

    Sub setmatchingconn(ByVal s As String)
        If s = "0000" Then
            Exit Sub
        End If
        Dim idx = 0
        For Each i As String In ListBox1.Items
            If i.StartsWith(s) Then
                Exit For
            End If
            idx += 1
        Next
        ListBox1.SelectedIndex = idx
    End Sub

    Dim currentlyloadedtileset = -1
    Sub loadtileset(ByVal q As Integer)
        If q = currentlyloadedtileset Then
            Exit Sub
        End If
        currentlyloadedtileset = q
        ' load tileset
        For i As Integer = 0 To 255
            Dim s = TILESET_PATH.Replace("%", q) & "\" & hex2(i) & ".png"
            tilesetimages(i) = New Drawing.Bitmap(s)
        Next
        Panel3.Invalidate()
    End Sub

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        ListBox1.Items.Clear()
        Dim d = My.Computer.FileSystem.GetFiles(BASE_PATH, FileIO.SearchOption.SearchAllSubDirectories, "*.asm")
        For Each i In d
            ListBox1.Items.Add(i.Replace(BASE_PATH & "\", ""))
        Next
        loadtileset(0)
        Panel3.HorizontalScroll.Visible = True
        Panel3.HorizontalScroll.SmallChange = 65
    End Sub

    Dim lastconn = 0

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        If lastconn = 1 Then
            Button6_Click(Nothing, Nothing)
            Exit Sub
        End If
        TextBox1.Text = connectionN_X
        TextBox2.Text = connectionN_Y
        setmatchingconn(hex4(connectionN))
        lastconn = 1
    End Sub

    Private Sub Button6_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button6.Click
        targetx = CInt(TextBox1.Text)
        targety = CInt(TextBox2.Text)
        Button1_Click(Nothing, Nothing)
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        If lastconn = 2 Then
            Button6_Click(Nothing, Nothing)
            Exit Sub
        End If
        TextBox1.Text = connectionS_X
        TextBox2.Text = connectionS_Y
        setmatchingconn(hex4(connectionS))
        lastconn = 2
    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        If lastconn = 3 Then
            Button6_Click(Nothing, Nothing)
            Exit Sub
        End If
        TextBox1.Text = connectionW_X
        TextBox2.Text = connectionW_Y
        setmatchingconn(hex4(connectionW))
        lastconn = 3
    End Sub

    Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
        If lastconn = 4 Then
            Button6_Click(Nothing, Nothing)
            Exit Sub
        End If
        TextBox1.Text = connectionE_X
        TextBox2.Text = connectionE_Y
        setmatchingconn(hex4(connectionE))
        lastconn = 4
    End Sub

    Private Sub Panel1_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Panel1.MouseMove
        Dim xx = Math.Floor(e.X / 16)
        Dim yy = Math.Floor(e.Y / 16)
        Dim xxx = Math.Floor(e.X / 32)
        Dim yyy = Math.Floor(e.Y / 32)
        Label2.Text = "X=" & xx & ", Y=" & yy
        If xx <> prevx Or yy <> prevy Then
            Panel1.Invalidate(New Drawing.Region(New Rectangle(hoverx * 16 - 1, hovery * 16 - 1, 16 + 2, 16 + 2)))
            hoverx = xx
            hovery = yy
            Panel1.Invalidate(New Drawing.Region(New Rectangle(hoverx * 16 - 1, hovery * 16 - 1, 16 + 2, 16 + 2)))
        End If
        prevx = xx
        prevy = yy
        If drawmode = 1 Then
            If replaceblock(xxx, yyy, curselblock) Then
                Panel1.Invalidate(New Drawing.Region(New Rectangle(xxx * 32, yyy * 32, 32, 32)))
            End If
        End If
    End Sub

    Private Sub ListBox1_MouseDoubleClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles ListBox1.MouseDoubleClick
        Button1_Click(Nothing, Nothing)
    End Sub

    Private Sub ListBox2_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ListBox2.SelectedIndexChanged
        If ListBox2.SelectedIndex = -1 Then
            Exit Sub
        End If
        TextBox3.Text = ListBox2.Items(ListBox2.SelectedIndex).ToString().Replace("hdr_object          ", "").Replace("hdr_signpost        ", "").Replace("hdr_warp            ", "")
        Panel1.Invalidate()
    End Sub

    Private Sub Button11_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button11.Click
        ListBox2.Items(ListBox2.SelectedIndex) = ListBox2.Items(ListBox2.SelectedIndex).ToString().Substring(0, "hdr_object          ".Length) & TextBox3.Text
        Panel1.Invalidate()
        writechangestofile()
    End Sub

    Private Sub TextBox3_KeyPress(ByVal sender As System.Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles TextBox3.KeyPress
        If e.KeyChar = Chr(13) Then
            Button11_Click(Nothing, Nothing)
        End If
    End Sub

    Private Sub Button10_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button10.Click
        If lastconn = 1 Then
            connectionN_X = CInt(TextBox1.Text)
            connectionN_Y = CInt(TextBox2.Text)
            connectionN = CInt("&H" & ListBox1.Items(ListBox1.SelectedIndex).ToString().Substring(0, 4))
        End If
        If lastconn = 2 Then
            connectionS_X = CInt(TextBox1.Text)
            connectionS_Y = CInt(TextBox2.Text)
            connectionS = CInt("&H" & ListBox1.Items(ListBox1.SelectedIndex).ToString().Substring(0, 4))
        End If
        If lastconn = 3 Then
            connectionW_X = CInt(TextBox1.Text)
            connectionW_Y = CInt(TextBox2.Text)
            connectionW = CInt("&H" & ListBox1.Items(ListBox1.SelectedIndex).ToString().Substring(0, 4))
        End If
        If lastconn = 4 Then
            connectionE_X = CInt(TextBox1.Text)
            connectionE_Y = CInt(TextBox2.Text)
            connectionE = CInt("&H" & ListBox1.Items(ListBox1.SelectedIndex).ToString().Substring(0, 4))
        End If
        writechangestofile()
    End Sub

    Sub updatecounts(ByVal str1 As String, ByVal str2 As String, ByVal str3 As String)
        Dim posAt = 0
        Dim cntAt = 0
        Dim total = 0
        For Each i As String In ListBox2.Items
            If i.Contains(str1) Then
                cntAt = posAt
            End If
            If i.Contains(str2) Then
                total += 1
            End If
            posAt += 1
        Next
        ListBox2.Items(cntAt) = str3 & total
    End Sub

    Private Sub Button7_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button7.Click
        Dim posAt = 0
        For Each i As String In ListBox2.Items
            If i.Contains("hdr_sign_count") Then
                Exit For
            End If
            posAt += 1
        Next
        ListBox2.Items.Insert(posAt + 1, "hdr_signpost        0, 0, $01")
        ListBox2.SelectedIndex = posAt + 1
        updatecounts("hdr_sign_count", "hdr_signpost ", "hdr_sign_count      ")
        Panel1.Invalidate()
        writechangestofile()
    End Sub

    Private Sub Button8_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button8.Click
        Dim posAt = 0
        For Each i As String In ListBox2.Items
            If i.Contains("hdr_object_count    ") Then
                Exit For
            End If
            posAt += 1
        Next
        ListBox2.Items.Insert(posAt + 1, "hdr_object          SPRITE_RED, 0, 0, STAY, NONE, $01")
        ListBox2.SelectedIndex = posAt + 1
        Panel1.Invalidate()
        updatecounts("hdr_object_count", "hdr_object ", "hdr_object_count    ")
        writechangestofile()
    End Sub

    Private Sub Button9_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button9.Click
        Dim posAt = 0
        For Each i As String In ListBox2.Items
            If i.Contains("hdr_warp_count      ") Then
                Exit For
            End If
            posAt += 1
        Next
        ListBox2.Items.Insert(posAt + 1, "hdr_warp            0, 0, 111, 111, $0000")
        ListBox2.SelectedIndex = posAt + 1
        Panel1.Invalidate()
        updatecounts("hdr_warp_count", "hdr_warp ", "hdr_warp_count      ")
        writechangestofile()
    End Sub

    Private Sub Button12_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button12.Click
        ListBox2.Items.RemoveAt(ListBox2.SelectedIndex)
        updatecounts("hdr_warp_count", "hdr_warp ", "hdr_warp_count      ")
        updatecounts("hdr_object_count", "hdr_object ", "hdr_object_count    ")
        updatecounts("hdr_sign_count", "hdr_signpost ", "hdr_sign_count      ")
        writechangestofile()
    End Sub

    Function replacewithhoverxy(ByVal q As Integer, ByVal s As String) As String
        Dim splitted = s.Split(",")
        For i As Integer = 0 To splitted.Length - 1
            If i = q Then
                If splitted(i).StartsWith(" ") Then
                    splitted(i) = " " & hoverx
                Else
                    splitted(i) = hoverx
                End If
            End If
            If i = q + 1 Then
                If splitted(i).StartsWith(" ") Then
                    splitted(i) = " " & hovery
                Else
                    splitted(i) = hovery
                End If
            End If
        Next
        Return Join(splitted, ",")
    End Function

    Private Sub Panel1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Panel1.Click
        If ListBox2.SelectedIndex = -1 Then
            Exit Sub
        End If
        If ListBox2.Items(ListBox2.SelectedIndex).StartsWith("hdr_warp") Then
            TextBox3.Text = replacewithhoverxy(0, TextBox3.Text)
        End If
        If ListBox2.Items(ListBox2.SelectedIndex).StartsWith("hdr_object") Then
            TextBox3.Text = replacewithhoverxy(1, TextBox3.Text)
        End If
        If ListBox2.Items(ListBox2.SelectedIndex).StartsWith("hdr_signpost") Then
            TextBox3.Text = replacewithhoverxy(0, TextBox3.Text)
        End If
        Button11_Click(Nothing, Nothing)
    End Sub

    Private Sub Button13_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button13.Click
        If ListBox2.SelectedIndex = -1 Then
            Exit Sub
        End If
        TextBox3.Text = ListBox2.Items(ListBox2.SelectedIndex).ToString().Replace("hdr_object          ", "").Replace("hdr_signpost        ", "").Replace("hdr_warp            ", "")
        Dim rnd As New Random()
        Dim rndindex = rnd.Next(0, sprites.Length)
        TextBox3.Text = TextBox3.Text.Replace("SPRITE_RED", sprites(rndindex))
    End Sub

    Private Sub Button14_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button14.Click
        Try
            Dim qx = TextBox3.Text.Split(",")(2)
            Dim qy = TextBox3.Text.Split(",")(3)
            Dim mapid = TextBox3.Text.Split(",")(4).Replace("$", "").Trim()
            targetx = CInt(qx)
            targety = CInt(qy)
            setmatchingconn(mapid)
        Catch ex As Exception
            Exit Sub
        End Try
        Button1_Click(Nothing, Nothing)
    End Sub

    Private Sub ListBox2_MouseDoubleClick(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles ListBox2.MouseDoubleClick
        Button14_Click(Nothing, Nothing)
    End Sub

    Private Sub Button15_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button15.Click
        Dim fname = BASE_PATH & "\" & ListBox1.Items(curmapindex)
        Shell("C:\prnp\pn.exe """ & fname & """")
    End Sub

    Private Sub ComboBox2_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ComboBox2.SelectedIndexChanged
        If ComboBox2.SelectedIndex = -1 Then
            Exit Sub
        End If
        Dim rgb = ComboBox2.Items(ComboBox2.SelectedIndex).ToString().Split(" ")(1).Split(",")
        ComboBox2.BackColor = Color.FromArgb(CInt(rgb(0)) * 8, CInt(rgb(1)) * 8, CInt(rgb(2)) * 8)
        If ComboBox1.SelectedIndex = -1 Then
            Exit Sub
        End If
    End Sub

    Private Sub ComboBox1_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ComboBox1.SelectedIndexChanged
        If ComboBox1.SelectedIndex = -1 Then
            Exit Sub
        End If
        If ComboBox2.SelectedIndex = -1 Then
            Exit Sub
        End If
    End Sub

    Private Sub Button16_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button16.Click
        writechangestofile()
    End Sub

    Private Sub Button17_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button17.Click
        Dim md = mapdata.Split(vbLf)
        Dim h = 0
        Dim w = 0
        For Each i In md
            If i.Length < 3 Then
                Continue For
            End If
            Dim isplit = i.Split(",")
            Dim x = 0
            h += 1
            w = 0
            For Each q In isplit
                w += 1
                x += 1
            Next
        Next
        Dim bm As New Bitmap(32 * w, 32 * h)
        Dim g = Graphics.FromImage(bm)
        Dim y = 0
        For Each i In md
            If i.Length < 3 Then
                Continue For
            End If
            Dim isplit = i.Split(",")
            Dim x = 0
            For Each q In isplit
                g.DrawImage(tilesetimages(CInt("&H" & q.Replace("$", ""))), x * 32, y * 32, 32, 32)
                x += 1
            Next
            y += 1
        Next
        bm.Save("C:\users\admin\desktop\" & ListBox1.Items(ListBox1.SelectedIndex) & ".png")
    End Sub

    Private Sub Panel3_Paint(ByVal sender As System.Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Panel3.Paint
        Dim g As Graphics = e.Graphics
        e.Graphics.TranslateTransform(Panel3.AutoScrollPosition.X, Panel3.AutoScrollPosition.Y)
        For i As Integer = 0 To 255
            g.DrawImage(tilesetimages(i), i * 65, 0, 64, 64)
            If curselblock = i Then
                g.DrawRectangle(Pens.Red, New Rectangle(i * 65, 0, 64, 64))
            End If
        Next
    End Sub

    Private Sub Panel3_MouseDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Panel3.MouseDown
        curselblock = Math.Floor((-Panel3.AutoScrollPosition.X + e.X) / 65)
        Panel3.Invalidate()
    End Sub

    Function replaceblock(ByVal changex As Integer, ByVal changey As Integer, ByVal block As Integer) As Boolean
        Dim md = mapdata.Split(vbLf)
        If changey >= md.Length Or changey < 0 Then
            Return True
        End If
        Dim xsplit = md(changey).Split(",")
        If changex >= xsplit.Length Or changex < 0 Then
            Return True
        End If
        Dim prev = xsplit(changex)
        xsplit(changex) = "$" & hex2(block)
        If prev = xsplit(changex) Then
            Return False
        End If
        md(changey) = String.Join(",", xsplit)
        mapdata = String.Join(vbLf, md)
        Return True
    End Function

    Private Sub Panel1_MouseDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Panel1.MouseDown
        If allowblockedit = 0 Then
            Return
        End If
        Dim changex = Math.Floor(e.X / 32)
        Dim changey = Math.Floor(e.Y / 32)
        If e.Button = Windows.Forms.MouseButtons.Right Then
            Dim md = mapdata.Split(vbLf)
            If changey >= md.Length Or changey < 0 Then
                Return
            End If
            Dim xsplit = md(changey).Split(",")
            If changex >= xsplit.Length Or changex < 0 Then
                Return
            End If
            Dim prev = xsplit(changex)
            curselblock = CInt("&H" & prev.Replace("$", ""))
            Panel3.Invalidate()
            Panel3.HorizontalScroll.Value = 65 * curselblock
            Return
        End If
        If replaceblock(changex, changey, curselblock) Then
            Panel1.Invalidate()
        End If
        drawmode = 1
    End Sub

    Private Sub Panel1_MouseUp(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles Panel1.MouseUp
        drawmode = 0
    End Sub

    Private Sub Button18_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button18.Click
        If allowblockedit = 1 Then
            allowblockedit = 0
            Button18.Text = "ENABLE block editing"
        Else
            allowblockedit = 1
            Button18.Text = "DISABLE block editing"
        End If
    End Sub

    Private Sub Button19_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button19.Click
        Dim w = CInt(InputBox("width?"))
        Dim h = CInt(InputBox("height?"))
        Dim nn = InputBox("name?")
        Dim t = CInt(InputBox("tileset id?"))
        Dim tpl = "SECTION ""XXX"", ROM0[$B800]" & vbLf
        tpl &= "" & vbLf
        tpl &= "X_Header:" & vbLf
        tpl &= "    hdr_tileset         " & t & vbLf
        tpl &= "    hdr_dimensions      " & w & ", " & h & "" & vbLf
        tpl &= "    hdr_palette         $00" & vbLf
        tpl &= "    hdr_music           $ff, $02" & vbLf
        tpl &= "    hdr_connection      NORTH, $0000, 0, 0" & vbLf
        tpl &= "    hdr_connection      SOUTH, $0000, 0, 0" & vbLf
        tpl &= "    hdr_connection      WEST,  $0000, 0, 0" & vbLf
        tpl &= "    hdr_connection      EAST,  $0000, 0, 0" & vbLf
        tpl &= "    " & vbLf
        tpl &= "X_Objects:" & vbLf
        tpl &= "    hdr_border          $00" & vbLf
        tpl &= "    hdr_warp_count      0" & vbLf
        tpl &= "    hdr_sign_count      0" & vbLf
        tpl &= "    hdr_object_count    0" & vbLf
        tpl &= "    " & vbLf
        tpl &= "X_RAMScript:" & vbLf
        tpl &= "    hdr_textptrs        $0000" & vbLf
        tpl &= "    rs_end" & vbLf
        tpl &= "" & vbLf
        tpl &= "X_Blocks:" & vbLf
        For i As Integer = 0 To h - 1
            tpl &= "db "
            For j As Integer = 0 To w - 1
                tpl &= ",$00"
            Next
            tpl = tpl.Replace("db ,", "    db ")
            tpl &= vbLf
        Next
        tpl &= "" & vbLf
        tpl &= "X_X:" & vbLf
        tpl &= "	ret" & vbLf
        tpl &= "" & vbLf
        My.Computer.FileSystem.WriteAllText(BASE_PATH & "\" & nn & ".asm", tpl, False)
        Form1_Load(Nothing, Nothing)
    End Sub

    Private Sub Button20_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button20.Click
        writechangestofile()
        Dim fname = BASE_PATH & "\" & ListBox1.Items(curmapindex)
        Dim fpold = My.Computer.FileSystem.ReadAllText(fname)
        Shell("""C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"" ""file://w:/code/fools2018_orig/mapeditor/ramscript.htm#" & fpold.Replace(vbLf, "`").Replace(vbCr, "") & """")
    End Sub

    Private Sub TextBox1_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox1.TextChanged

    End Sub

    Private Sub TextBox4_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox4.TextChanged
        borderblock = CInt(TextBox4.Text)
    End Sub

    Private Sub Button21_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button21.Click
        TextBox4.Text = curselblock
        borderblock = curselblock
    End Sub

    Private Sub TextBox5_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox5.TextChanged

    End Sub

    Private Sub Button22_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button22.Click
        Shell("cmd /c cd /d W:\code\fools2020\mapsraw && envc && python 18to20.py """ & ListBox1.Items(curmapindex) & """")
    End Sub
End Class
