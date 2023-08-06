#!/usr/bin/osascript

on run argv
    try
        if count of argv is 0 then --close current tab
            tell application "Brave Browser"
                if count of window is not 0 then
                    tell active tab of front window to close
                end if
            end tell
            return
        end if --close by url
        tell application "Google Chrome"
            repeat with _url in argv
                repeat with w in every window
                    repeat with t in every tab in w
                        if _url is in (URL of t as text) then
                            tell t to close
                        end if
                    end repeat
                end repeat
            end repeat
        end tell
    on error errorMessage number errorNumber
        if (errorNumber is equal to -609) --Google Chrome got an error: Connection is invalid
            return
        end if
        error errorMessage number errorNumber
    end try
end run
