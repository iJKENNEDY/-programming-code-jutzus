package kotlin_script

fun main(args: Array<String>){

    // var -> is a mutable variable
    // val -> is used to declare a read-only variable
    val name = "enigma-code"
    var name2: String = "kotlin"
    println(name+ " != "+ name2)

    // Numbers::-> Long(64), Int(32), Short(16), Byte(8), Double(64), Float(32)
    val int = 123
    val long = 123456L
    val double = 12.34
    val float = 12.34F
    val hexadecimal = 0xAB
    val binary = 0b01010101

    //functions for conversions between types is toByte(), toShort(), toInt(),
    //          toLong(), toFloat(), toDouble(), toChar().
    val long2 = int.toLong()

    //booleans
    val x1 = 12
    val y1 = 43
    val z1 = 44

    val isTrue = x1 < y1 && x1 < z1
    println(isTrue)

    val alsoTrue = x1 == y1 || y1 == z1
    println(alsoTrue)

    //Chars-char::: escaping(( \t, \b, \n, \r, '. '', \\, \$

    //Strings
    val string = "enigma code \nin kotlin"
    val rawString= """
        raw string is super useful for strings...
    """.trimIndent()
    println(string)
    println(rawString)
    println()


    //Arrays> create an array using function--> arrayOf()
    val array = arrayOf(1,2,4)

    val perfectSquares = Array(10, {k -> k * k})

    // expressions can be embedded ($)
    val nameCode = "Kotlin"
    val str_ = "My favorite code is $nameCode. numbers of caracters is ${nameCode.length}"
    println(str_)

    // Ranges___
    val aToz = "a".."z"
    val oneToNine = 1..9
    println(aToz)
    println(oneToNine)

    //..Loops


    val list = listOf(1,2,3,4)
    for (k in list){
        println(k)
    }

    println()
    val list2 = listOf(22,34,54,665,76,21,3,5,6,7)
    for (l in list2){
        println(l)
    }

    println()

    val setValues = setOf(23,3,342,54,2765,6544,32)
    for (aa in setValues){
        println(aa)
    }

    val oneToTen2 = 1..10
    for (k in oneToTen2){
        println(k)
    }

    val setValues4 = setOf(23,432,44,543,76,75,23,34,6)
    for (a3 in setValues4){
        print(a3)
        print("-")
    }

    val  oneToTwenty = 1..20
    for (l2 in oneToTwenty){
        println(l2)
    }

    val string = "maquina enigma"
    for (char in string){
        println(char)
    }

    for (index in string.indices){
        println("Element $index is ${string[index]}")
    }

    val parrafo = "codigo-enigma"
    for (parr in parrafo.indices){
        println("elements $parr is ${parrafo[parr]}")
    }
}