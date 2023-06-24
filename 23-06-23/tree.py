Families={'teju':
                 {'teddy bear':{'chicken','Bts'},
                  'BTS':{'taekook'}},
          'Yochana':
                 {'Asha':{'Rishik'},
                  'Gayathri':{'Sai'},
                  'Uma':{'Rahul'}},
          'Ankitha':
                  {'Rishi':'Ankitha','BTS':'RM'}
          }
for parent,Friends in Families.items():
    print(f"{parent} has {len(Friends)} favorites(s):")
    print(f" {',and '.join([str(child) for child in [*Friends]])}")