core.register_fetches("choose_backend", function(txn)
    local path = txn.sf:path()
 
    if path:find("/app", 1, true) == 1 then
       return "my_apps"
    elseif path:find("/img", 1, true) == 1 then
       return "img_apps"
    else
       return "my_apps" -- Default backend
    end
 end)
 