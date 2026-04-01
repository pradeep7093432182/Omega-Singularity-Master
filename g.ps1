param(
    [Parameter(ValueFromRemainingArguments=$true)]
    $RemainingArgs
)

python "D:\antigravity\TermuxCLI\g_core.py" $RemainingArgs
