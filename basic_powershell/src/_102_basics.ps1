#comparaciones
<#
$valor1 = 12
$valor2 = 44

$valor1 -eq $valor2
$valor1 -ne $valor2
$valor1 -gt $valor2
$valor1 -ge $valor2
$valor1 -lt $valor2
$valor1 -le $valor2
#>
# =, -=, +=
# -not, -or, -and


#listas::
<#
$myList = @(0..4)

Write-Host("print array")
$myList

$myList = @(0..4)

Write-Host("Assign values")
$myList[1] = 10
$myList
#>


#...........................
#...........................
<#
Write-Output "SCIENCE computing"
Echo "qwerty19"
Write "enigma 123"
$mensaje = Write-Output "owlTech27"
$mensaje
#>

#------------------------
#__ creating objects ___
#------------------------

# New-object -> cmdlet is used to create an object
$var = New-Object System.DateTime

#calling constructo with parametes 
$sr = New-Object System.IO.StreamReader -ArgumentList "file path"

#...
$newObject = New-Object -TypeName PSObject -Property @{
    ComputerName = "SERVER1"
    Role = "Interface"
    Enviromment = "Production"
}
$newObject
#..
$newObject = [PSCustomObject]@{
   ComputerName = 'server2'
   Role = 'Interface'
   Environment = 'Production'   
}


#.....
Get-ChildItem | Select-Object FullName, Name,
    @{Name='DateTime'; Expression={Get-Date}},
    @{Name='PropertyName'; Expression={'CustomValue'}}


#.................................
#..... variables powershell ......
#.................................
$foo = "bar"

###..arrays.....
$myArrayIfInts = 1,2,3,4
$myArrayOfStrings = "1","2","3","4","5"

#adding to an array
$myArrayIfInts = $myArrayIfInts + 5

#combining arrays together
$myArrayOfInts = 1,2,3,4
$myOtherArrayOfInts = 5,6,7
$myArrayOfInts= $myArrayOfInts + $myOtherArrayOfInts

###..............................................
#.... list assignement of multiple variables ....
#................................................
$input = "foo.bar.baz"
$parts = $input.Split(".")

##...Scope....
$foo = "Global Scope"
function myFunc{
    $foo= "Function (local) scope"
    Write-Host $global:foo
    Write-Host $local:foo
    Write-Host $foo
}
myFunc
Write-Host $local:foo
Write-Host $foo

#.....Removing a variable
#Remove-Item Variable:\foo
$var = "Some Variable"
$var

Remove-Variable -Name var
$var


#....operators-----
#-comparison operators...(-)(eq,gt,..)
#..names can be preceded by special characters to modify the behavior of the operator
######..i....case-Insensitive Explicit (-ieq)
######..c....case-Sensitive Explicit (-ceq)
##__simple comparison operators
2 -eq 2 # Equal to (==)
2 -ne 4 # Not equal to (!=)
5 -gt 2 # Greater-than (>)
5 -ge 5 # Greater-than or equal to (>=)
5 -lt 10 # Less-than (<)
5 -le 5 # Less-than or equal to (<=)
##-__string comparison operators
"MyString" -like "*String"
"MyString" -notlike "Other*"
"MyString" -match "^String$"
"MyString" -notmatch "^Other$"

#... collection comparison operators
"abc", "def" -contains "def"
"abc", "def" -notcontains "123"
"def" -in "abc","def"
"123" -notin "abc", "def"

#... arithmetic operators.. (+,-,*,/,%,)
100 -shl 3 #bitwise shift-left
100 -shr 1 #bitwise shift-right

#... assignment operators
$var = 1 #assigment
$var += 2 #addition
$var -= 1 #subtraction
$var *= 2 #multiplication
$var /= 2 #division
$var %= 2 #modulus
#increment and decrement
$var++
$var--
#
#------ Redirection Operators ----
cmdlet > file # Send success output to file, overwriting existing content
cmdlet >> file # Send success output to file, appending to existing content
cmdlet 1>&2 # Send success and error output to error stream
#Error output stream:
cmdlet 2> file # Send error output to file, overwriting existing content
cmdlet 2>> file # Send error output to file, appending to existing content
cmdlet 2>&1 # Send success and error output to success output stream
#Warning output stream: (PowerShell 3.0+)
cmdlet 3> file # Send warning output to file, overwriting existing content
cmdlet 3>> file # Send warning output to file, appending to existing content
cmdlet 3>&1 # Send success and warning output to success output stream
#Verbose output stream: (PowerShell 3.0+)
cmdlet 4> file # Send verbose output to file, overwriting existing content
cmdlet 4>> file # Send verbose output to file, appending to existing content
cmdlet 4>&1 # Send success and verbose output to success output stream
#Debug output stream: (PowerShell 3.0+)
cmdlet 5> file # Send debug output to file, overwriting existing content
cmdlet 5>> file # Send debug output to file, appending to existing content
cmdlet 5>&1 # Send success and debug output to success output stream
#Information output stream: (PowerShell 5.0+)
cmdlet 6> file # Send information output to file, overwriting existing content
cmdlet 6>> file # Send information output to file, appending to existing content
cmdlet 6>&1 # Send success and information output to success output stream
#All output streams:
cmdlet *> file # Send all output streams to file, overwriting existing content
cmdlet *>> file # Send all output streams to file, appending to existing content
cmdlet *>&1 # Send all output streams to success output stream

#-- mixing operand types...
#.for addition
"3" + 2
4 + "2"
1,2,3 + "enigma"
"qwerty"+ 1,2,3
#.for multiplication
"3" * 2
2*"3"
1,2,3 * 2
2 * 1,2,3 #error

#....
$a = Read-Host "Enter a number"
$a -gt 5


# Logical Opertors
-and #logical and
-or  #logical or
-xor #logical exclusive or
#. -not or ! # Logcal not


#.......................
#-- string manipulation operators
"the rain in Seatle" -replace 'rain','hail'
"enigma@contoso.com" -replace '^[\w]+@(.+)', '$1'
#.... -split
"A B C" -split " "
"e", "g", "g" -join ":"



###### .. Special Operators....
#_ Array Expression Operator
#return the expression as an array
@(Get-ChildItem $env:windir\System32\ntdll.dll)
#will return an array with one item
@(Get-ChildItem $env:windir\System32)

###### .. call operation ...
$command = 'Get-ChildItem'
& $command


################################
##### chapter 5 ###############
#... basic set operation.....
#...........................
#####.filtering: where-object/ where/?
#..Where-Object... where... ?
$names = @("Elva","Aldo","Ariana","Ramit","Anali","Wasli","kiara","Jasmin")
$names
$names | Where-Object{$_ -like "E*"}
$names | where {$_ -like "A*"}
$names | ? {$_ -like "A*"}

#####.ordering:sort-object/sort
#... Sort-Object, ...sort
$names = @("Elva","Aldo","Ariana","Ramit","Anali","Wasli","kiara","Jasmin")
$names | Sort-Object
$names | sort
#.to reques descending order:
$names | Sort-Object -Descending
$names | Sort -Descending

$names | Sort-Object {$_.length}

#### grouping: Group-object/ group
#..Group-Object ... group
$names = @("Elva","Aldo","Ariana","Ramit","Anali","Wasli","kiara","Jasmin")
$names | Group-Object -Property Length
$names | group -Property Length


##### projecting: select-object / select
#.. select-Object ... SELECT
$dir = dir "C:\pyWeb"

$dir | Select-Object Name, Fullname, Attibutes
$dir | select Name, Fullname, Attributes

$dir | select -First 1 *


##----------------------------------------
##------ cap 6 - conditional logic -------
##----------------------------------------
#.. if, else and else if
$test = "test"
if($test -eq "test"){
    Write-Host "If condition met"
}
#...
$test = "test"
if($test -eq "test2"){
    Write-Host "if condition met"
}
else{
    Write-Host "if condition not met"
}

#....
$test = "test"
if ($test -eq "test2"){
    Write-Host "if condition met"
}
elseif($test -eq "test"){
    Write-Host "ifelse condition met"
}


#####...Negation....
$test = "test"
if (-Not $test -eq "test2"){
    Write-Host "if condition not met"
}

#..!
$test = "test"
if (!($test -eq "test2")){
    Write-Host "if condition not met"
}

#.. -ne ...
$test = "test"
if($test -ne "test2"){
    Write-Host "Variable test is not equal to 'test2'"
}

####.. If conditional shorthand
#Done in Powershell 2.0
$boolean = $false;
$string = "false";
$emptyString = "";
If($boolean){
# this does not run because $boolean is false
Write-Host "Shorthand If conditions can be nice, just make sure they are always boolean."
}
If($string){
# This does run because the string is non-zero length
Write-Host "If the variable is not strictly null or Boolean false, it will evaluate to true as
it is an object or string with length greater than 0."
}
If($emptyString){
# This does not run because the string is zero-length
Write-Host "Checking empty strings can be useful as well."
}
If($null){
# This does not run because the condition is null
Write-Host "Checking Nulls will not print this statement."
}


#..................................
#....... cap-7 Loops ..............
#..................................
#...Foreach
$names = @('Amy','Bod','Celine','David','Kennedy')
ForEach ($name in $names)
{
    Write-Host "Hi, my name is $name!"
}

#......
$Numbers = ForEach($Number in 1..20){
    $Number
}
$Numbers

#.......
$Numbers = @()
ForEach ($Number in 1..20)
{
    $Numbers += $Number
}
$Numbers
#.............
#....For......
for($i=0; $i -le 5; $i++){
    "$i"
}

#..ForEach() Method
(1..10).ForEach({$_ * $_})
#or
(1..10).ForEach{$_ * $_}

