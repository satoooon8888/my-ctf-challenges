# vulneability
JSONの型チェックを行っていないため、文字列ではなく配列や連想配列を送ることができる点。

# solution
`input_pass[i] in "0oO"`で、`input_pass[i]`が数値のときにエラーになることを利用する。
`{"pass": ["a", 1, ..., 1]}`というJSONを送ると`"a" != password[0]`のときに`return False`でループが打ち切られ401を返し、`"a" == password[0]`のときには次のループに入り18行目で`500 Internal Server Error`が発生する。
500を返すか401を返すかで`password[0]`を判定でき、この一種のオラクルを使えばError-based Blind SQL Injectionのようなことができる。先頭からパスワードを一文字ずつ探索してパスワードを確定させればよい。
