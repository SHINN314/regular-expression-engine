/* テキスト中にある正規表現を探索 */
int match (char *regexp, char *text) {
    if (regexp[0] == '^') {
        //　文字列の先頭を確認
        return matchhere(regexp + 1, text);
    }

    do {
        if (matchhere(regexp, text)) {
            return 1;
        }
    } while (*text++ != '\0');

    return 0;
}

int matchhere (char *regexp, char *text) {
    if (regexp[0] == '\0') {
        // 空チェック(すべての文字列を受理する)
        return 1;
    }
    if (regexp[1] == '*') {
        // 繰り返しチェック
        return matchstar(regexp[0], regexp + 2, text);
    }
    if (regexp[0] == '$' && regexp[1] == '\0') {
        // 末尾チェック
        return *text == '\0';
    } 
    if (*text != '\0' && (regexp[0] == '.' || regexp[0] == *text)) {
        // 任意の文字チェック
        return matchhere(regexp + 1, text + 1);
    }

    return 0;
}

int matchstar (int c, char *regexp, char *text) {
    do {
        if (matchhere(regexp, text)) {
            return 1;
        } 
    } while (*text != '\0' && (*text++ == c || c == '.'));

    return 0;
}