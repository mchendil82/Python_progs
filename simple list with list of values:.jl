simple list with list of values:
==========================
simple_list=[0,1,2,3]  #--> list of  Numeric/digit values (or list of "int" data type values) -> no elemments/values 4 (seperated by  comma)
index/position-0: 1
index-1: 2
index-2: 3
simple_list=["test", "test2", "test3"] #---> list of words (or list of "string" data type values) -> no elements/values 3 (seperated by  comma)
index-0

simple list with simple one or more dict
======================
simple_list_with_simple_dict=[{"a":"1"}] #---> No elements/values : 1 ----> one dict defined (seperated byt comma)
simple_list_with_multiple_dict=[{"a":"1"},{"b":"2"}] #---> No elements/values : 2 ----> 2 dict defined (seperated byt comma)
simple_list_with_multiple_dict_each_dict_has_multiple_keypair_values=[{"a":"1","aa":"11","aaa":"111"},{"b":"2","bb":"22","bbb":"222"},{"c":"3","cc":"33","ccc":"333"}] #--> No elements/values : 3 ----> 3 dict defined (seperated byt comma)


simple dict with key,pair values:
=======================================
simple_dict= {"xx": "11", "yy":"22"} #---> simple dict with more than 2 key pair values ---> with each key has string values
simple_dict_with_simple_list_in_one_key: {"xx": ["0","1","2"],"yy":"22"} #--> #---> simple dict with more than 2 key pair values ---> 1st key has list of values and the list has 3 elements
                                                                              #---> and 2nd element has string value


simple_dict_wth_multiple_dict= {"xx":{"a":"1"},"yy": {"b":"2"}} #----> dict of dict --> master dict 2 items and each item is dict 
                                                     # 1st key is a dict and it has 1 key pair value with string data type in value
                                                    # 2nd  key is a dict and it has 1 key pair with string data type in value




simple_list=[1,2,3,4]

for each_item in simple_list:
    totally 4 items = 4 time should Loop 
    1st time each_item= 0 (index=0)
    2nd time each_item=1 (index=1)


  simple_list_with_simple_dict=[{"a":"1"}]

  for each_item in simple_list_with_simple_dict:
    totally only 1 item is there
    1st time each_item will have dict : {"a":"1"}
    loop will end
    if I need to access dict a value then I have say each_item["a"]



simple_dict_with_simple_list_in_one_key: {"xx": ["0","1","2"],"yy":"22"} 

for each_item in simple_dict_with_simple_list_in_one_key:
    totally only 2 items is there
    1st time "each_item" will have key : xx - only key value will be there because it is a dict and I am not use  item()
    2nd time "each_item" will have key : yy - only key value will be there because it is a dict and I am not use  item()




simple_dict_with_simple_list_in_one_key: {"xx": ["0","1","2"],"yy":"22"} 

for each_item,each_value in simple_dict_with_simple_list_in_one_key.items():
    totally only 2 items is there and I am using items funtion bring each key into variable called "each_item"
      and value will be in the variable called "each_value"..
    1st time "each_item" will have key  : xx - only key value will be there 
        "each_value" will have value is: ["1","2","3"]  
         if I need to print number "3" print value in the list the "index number is 2": each_value[2]       
    2nd time "each_item" will have dict : yy - 
        "each_value" will have value is: 22
     

    

    .....
