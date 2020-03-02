package kotlin_script

import sun.jvm.hotspot.interpreter.Bytecodes
import java.io.IOException
import java.nio.file.Files
import java.nio.file.Path

fun readFile(path: Path): Unit{
    val input = Files.newInputStream(path)
    try{
        var byte = input.read()
    while (byte != -1){
        println(byte)
        byte = input.read()
    }
    }catch (e: IOException){
        println("Error reading from file.")
    }finally {
        input.close()
    }
}




//Referential equality and structural equality
//val a  = File("/enigma.doc")
//val b = File("codeenigma.doc")
//val sameRef = a ===b
//val structural = a==b

// conttrol flow as expressions
// val date = Date()
// val today = if (date.year == 2016) true else false

fun isZero (x: Int): Boolean {
    return if(x==0)true else false
}

//used for try..catch
/*
val succss = try{
    readFile()
    true
    } catch (e: IOException){
    false
}*/

// nUll syntax
var str: String? = null
//var str2: String = null

fun isString (any: Any): Boolean{
    return if (any is String) true else false
}

// smart  casts
fun printStringLength(any: Any){
    if (any is String){
        println(any.length)
    }
}

fun isEmptyString(any: Any): Boolean{
    return any is String && any.length==0
}

//explitic casting
fun length(any: Any):Int{
    val string = any as String
    return  string.length
}

//..When..expression...
fun whatNumber(x: Int){
    when(x){
        0 -> println("x is zero")
        1 -> println("x is 1")
        else -> println("X is neither 0 or 1")
    }
}


fun isMinOrMax(x: Int): Boolean{
    val isZero = when(x){
        Int.MIN_VALUE -> true
        Int.MAX_VALUE -> true
        else -> false
    }
    return isZero
}

fun isZeroOrOne(x: Int): Boolean{
    return when(x){
        0, 1 -> true
        else -> false
    }
}

fun isAbs(x: Int): Boolean {
    return when(x){
        Math.abs(x) -> true
        else -> false
    }
}

fun isSingleDigit(x: Int): Boolean{
    return when(x){
        in -9..9 -> true
        else -> false
    }
}

fun isDieNumber(x: Int): Boolean{
    return when(x){
        in listOf(1,2,3,4,5,6)-> true
        else ->false
    }
}


fun startsWithFoo(any:Any): Boolean{
    return when (any){
        is String -> any.startsWith("Foo")
        else -> false
    }
}

//..when_without_argument
fun whenWithoutArgs(x: Int, y:Int){
    when{
        x < y -> println("x is less than y")
        x > y -> println("x is greater than y")
        else -> println("X must equal Y")
    }
}

//function return
fun addTwoNumbers(a: Int, b: Int): Int{
    return a + b
}

fun largestNumber(a:Int, b:Int, c:Int): Int{
    fun  largest(a: Int, b:Int): Int {
        if (a > b) return a
            else return b
    }
    return largest(largest(a,b), largest(b,c))
}

fun printLessThanTwo(){
    val list = listOf(1,2,3,4)
    list.forEach(fun(x){
        if (x < 2) println(x)
        else return
    })
    println("This line will still execute")
}