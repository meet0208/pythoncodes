color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

dictionary_items =color_dict.items()
sorted_items = sorted(dictionary_items)
print(sorted_items)

#or

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))