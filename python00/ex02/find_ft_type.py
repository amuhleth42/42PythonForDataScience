def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    name = type_names.get(type(object), "NotFound")
    if (name == "String"):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (name == "NotFound"):
        print("Type not found")
    else:
        print(f"{name}: {type(object)}")
    return 42
