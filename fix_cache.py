import glob

css_target = 'href="assets/css/style.css"'
css_replacement = 'href="assets/css/style.css?v=2.0"'

js_target = 'src="assets/js/main.js"'
js_replacement = 'src="assets/js/main.js?v=2.0"'

for file in glob.glob('d:/work/focuspointacademy/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if css_target in content:
        content = content.replace(css_target, css_replacement)
        modified = True
        
    if js_target in content:
        content = content.replace(js_target, js_replacement)
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated cache-busters in {file}")
