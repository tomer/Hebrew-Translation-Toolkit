#rm hspell.text.tmp
#find he -type f \( -name "*.php" -o -name "*.txt" \) -print -exec ./spell-check.sh {}  \;
#iconv -t windows-1255 hspell.text | hspell -ia | iconv -f windows-1255 | sort > hspell.text

#cat hspell.text.tmp | grep -v '^\*?$' | sort > hspell.text
#cat hspell.text.tmp | tr -d '^*$' | grep -v '^$' | sort > hspell.text

find he -type f \( -name "*.php" -o -name "*.txt" \) -exec iconv -t windows-1255 {} \; | hspell -c | iconv -f windows-1255 | sort -n > hspell.txt
