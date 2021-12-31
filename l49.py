color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result=[{'color_name':i,'color_code':j} for i,j in zip(color_name,color_code)]
print(result)