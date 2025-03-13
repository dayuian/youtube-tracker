# visual.py
import streamlit.components.v1 as components

def odometer_component(value: int):
    """
    顯示滾動數字動畫（使用 Odometer.js）
    """
    components.html(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/odometer.js/0.4.8/themes/odometer-theme-default.min.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/odometer.js/0.4.8/odometer.min.js"></script>
            <style>
                .odometer {
                    font-size: 72px;
                    color: #2196F3;
                    font-weight: bold;
                    text-align: center;
                    margin: 1em auto;
                }
            </style>
        </head>
        <body>
            <div id="odometer" class="odometer">0</div>

            <script>
                setTimeout(function(){
                    document.getElementById("odometer").innerHTML = "%s";
                }, 300);
            </script>
        </body>
        </html>
        """ % value,
        height=180,
    )
