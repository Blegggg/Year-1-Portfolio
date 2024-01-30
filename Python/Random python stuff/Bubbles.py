def bubble_sort(items): 

   num_items = len(items) 
   passes = 1 
   while passes < num_items: 

       for current in range(num_items - passes): 

            if items[current] > items[current+1]: 

                temp = items[current] 

                items[current] = items[current+1] 

                items[current+1] = temp 
                passes = passes + 1 