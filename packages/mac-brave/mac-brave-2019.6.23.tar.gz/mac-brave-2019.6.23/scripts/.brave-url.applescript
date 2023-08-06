#!/usr/bin/osascript

try
  tell application "Brave Browser"
    if count of windows is not 0 then return URL of active tab of first window
  end tell
on error errorMessage number errorNumber
  if (errorNumber is equal to -609) --Connection is invalid
    return
  end if
  error errorMessage number errorNumber
end try
