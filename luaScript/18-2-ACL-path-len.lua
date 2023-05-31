core.register_fetches("choose_backend", function(txn)
    local path = txn.sf:path()
 
    if path:sub(1, 4) == "/app" then
       return "my_apps"
    elseif #path == 14 then
       return "img_apps"
    else
       return "my_apps" -- Default backend
    end
 end)
 