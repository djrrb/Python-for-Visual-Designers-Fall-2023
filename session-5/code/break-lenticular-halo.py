myPath = 'Juvenile_Ragdoll.jpg'

myImage = ImageObject(myPath)
myImage.lenticularHaloGenerator(size=(1000, 1000), center=None, color=None, haloRadius=40, haloWidth=500, haloOverlap=None, striationStrength=0, striationContrast=-48, time=0)


newPage(*myImage.size())
image(myImage, (0, 0))