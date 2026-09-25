param([string]$DocPath, [string]$PdfPath)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($DocPath)
$doc.Repaginate()
$pages = $doc.ComputeStatistics(2)
Write-Output "PAGES: $pages"
Write-Output "--- Hyperlinks ---"
foreach ($h in $doc.Hyperlinks) {
    Write-Output "$($h.TextToDisplay)  ->  $($h.Address)"
}
$doc.SaveAs([ref]$PdfPath, [ref]17)
$doc.Close($false)
$word.Quit()
Write-Output "Exported PDF to $PdfPath"
