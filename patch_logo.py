with open("index.html", "r") as f:
    content = f.read()

search_str = """
                        switch(col.id) {
                            case 'Name':
                                val = `<div style="display:flex; align-items:center;">${getLogoHtml(t)}${perfData.name}</div>`;
                                break;
                            case 'Ticker': val = t; break;
"""
replace_str = """
                        switch(col.id) {
                            case 'Name':
                                val = `<div style="display:flex; align-items:center; width:100%; justify-content:space-between;">
                                         <div style="display:flex; align-items:center;">${getLogoHtml(t)}${perfData.name}</div>
                                         <i class="material-icons" style="font-size:16px; color:#999; cursor:pointer;" onclick="event.stopPropagation(); analyzeTickerChart('${t}')" title="AI Summary for ${perfData.name}">auto_awesome</i>
                                       </div>`;
                                break;
                            case 'Ticker': val = t; break;
"""
if search_str in content:
    content = content.replace(search_str, replace_str)
    with open("index.html", "w") as f:
        f.write(content)
    print("Patch applied successfully.")
else:
    print("Search string not found.")
