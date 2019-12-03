#PDXScript++ list of syntactical sugar and improvements

Note: everything surrounded by < > is a variable and is to be replaced by your own value

* Better `if` statements:

        if <condition> = {
            <function>
        }

        translates to 
        
        if = {
            limit = {
                <condition>
            }
            <function>
        }
        
        

* Switch statements:

       switch <var_name> = {
           case <var_value> = {
               <function>
           }
           
           case <var_value> = {
               <function>
           }
       }