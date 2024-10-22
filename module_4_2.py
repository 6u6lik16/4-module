def test_function():
    def  inner_function():
        print("Я в области действия test_function" )
    inner_function()



test_function()
inner_function() # Ошибка, т к inner_function доступен только внутри test_function