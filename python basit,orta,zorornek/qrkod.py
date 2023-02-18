import qrcode
data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"
image = qrcode.make(data)
image.save("my.png")
