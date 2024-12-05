build:
	 gcc -D_FORTIFY_SOURCE=2 -O2 pinzoro.c -o pinzoro
	 patchelf --replace-needed libc.so.6 ./libc.so.6 --set-interpreter ./ld-2.31.so pinzoro
