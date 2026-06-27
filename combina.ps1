$html = Get-Content "c:\projetos\novoprojeto\index.html" -Raw -Encoding UTF8
$css = Get-Content "c:\projetos\novoprojeto\style.css" -Raw -Encoding UTF8
$js = Get-Content "c:\projetos\novoprojeto\script.js" -Raw -Encoding UTF8

$html = $html -replace '<link rel="stylesheet" href="style.css">', "<style>$css</style>"
$html = $html -replace '<script src="script.js"></script>', "<script>$js</script>"

$html | Set-Content "c:\projetos\novoprojeto\index-unico.html" -Encoding UTF8
Write-Host "Arquivo unico criado: index-unico.html"
Write-Host "Tamanho: $($html.Length) caracteres"
