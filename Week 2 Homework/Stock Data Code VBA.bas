Attribute VB_Name = "Module1"
Sub stockdata2016()
Dim stock_name As String
Dim stock_total As Double

Dim summary_table_row As Double
summary_table_row = 2

For r = 2 To 797711
    If Cells(r + 1, 1).Value <> Cells(r, 1).Value Then
        stock_name = Cells(r, 1).Value
        stock_total = stock_total + Cells(r, 7).Value
        Range("I" & summary_table_row).Value = stock_name
        Range("J" & summary_table_row).Value = stock_total
        summary_table_row = summary_table_row + 1
        stock_total = 0
        
    Else
        stock_total = stock_total + Cells(r, 7).Value
        
    End If
    
    Next r
    
        
        
         
End Sub
Sub stockdata2015()
Dim stock_name As String
Dim stock_total As Double

Dim summary_table_row As Double
summary_table_row = 2

For r = 2 To 760192
    If Cells(r + 1, 1).Value <> Cells(r, 1).Value Then
        stock_name = Cells(r, 1).Value
        stock_total = stock_total + Cells(r, 7).Value
        Range("I" & summary_table_row).Value = stock_name
        Range("J" & summary_table_row).Value = stock_total
        summary_table_row = summary_table_row + 1
        stock_total = 0
        
    Else
        stock_total = stock_total + Cells(r, 7).Value
        
    End If
    
    Next r
    
End Sub
Sub stockdata2014()
Dim stock_name As String
Dim stock_total As Double

Dim summary_table_row As Double
summary_table_row = 2

For r = 2 To 705714
    If Cells(r + 1, 1).Value <> Cells(r, 1).Value Then
        stock_name = Cells(r, 1).Value
        stock_total = stock_total + Cells(r, 7).Value
        Range("I" & summary_table_row).Value = stock_name
        Range("J" & summary_table_row).Value = stock_total
        summary_table_row = summary_table_row + 1
        stock_total = 0
        
    Else
        stock_total = stock_total + Cells(r, 7).Value
        
    End If
    
    Next r
    
        
End Sub
