# 脆弱性

file_get_contentsにそのまま入力を渡しているところにディレクトリトラバーサルの脆弱性がある。

# 解法

Dockerfileを見ればflag.txtがresourceの上にあるので、`../flag.txt`でフラグが手に入る。