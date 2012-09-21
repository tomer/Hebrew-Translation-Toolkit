rm -rf new
find he -type f \( -name "*.php" -o -name "*.txt" \) -print -exec  python replace.py {} \;
meld new/he he
