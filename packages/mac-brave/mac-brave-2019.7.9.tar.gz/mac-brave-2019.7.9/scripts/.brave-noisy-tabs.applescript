#!/usr/bin/osascript

property _TIMEOUT_APP: 5
property _TIMEOUT_TAB: 1

try
  with timeout of _TIMEOUT_APP seconds
    tell application "Brave Browser"
      repeat with w in every window
        repeat with t in every tab of w
          with timeout of _TIMEOUT_TAB seconds
            tell t
              if loading of t is false then
                set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('audio,video'),function(elem){return elem.duration > 0 && !elem.paused})"
                if is_playing is true then
                  log (get url of t)
                end if
              end if
            end tell
          end timeout
        end repeat
      end repeat
    end tell
  end timeout
on error errorMessage number errorNumber
  --Connection is invalid. (-609)
  if (errorNumber is in {-609}) then return
  error errorMessage number errorNumber
end try
