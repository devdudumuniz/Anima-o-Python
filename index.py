#Created By MR.DD

import os
print("""
<body>
<p>🧘‍♂️</p>       
</body>""")

print("""<style>
html {height:600px;
}
body {
background-color:#333;
}   

p {position:fixed;
top:30%;
left:30%;
font-size:90px;
transform:scale(0.85, 0.85);
animation: Bit 1s linear -1s infinite normal;
}

@keyframes Bit {
50% { transform: scale(1, 1);} 
}

img{display:none;}
</style>""")

print("""<script>
window.onload=function(){    
let i = 100;
let id = setInterval(function() {
    i--;    
    if (i == -1) {
        clearInterval(id);     
    } else {
navigator.vibrate&&navigator.vibrate(50);  
    }
  }, 1000);      
}
</script>""")
os.system("touch file.png")

