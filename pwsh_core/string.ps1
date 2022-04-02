# string creation
$FirstName = "Jobin"
$SurName = "Nelson"

# String concatination
"Hi, my name is " + $FirstName + " and my surname is " + $SurName.ToUpper() 

# String interpolation
"Hi, my name is $FirstName and my surname is $($SurName.ToUpper())."

# -f
"Hi, my name is {0} and my surname is {1}" -f $FirstName, $SurName.ToUpper()

# Quotation marks
"$FirstName $SurName"
'$FirstName $SurName'
'{0} {1}' -f $FirstName, $SurName

# Joining string
$FullName = "$FirstName $SurName"
$FullName

# String as array
$FullName[0]
$FullName[-1]
$FullName[0..2]

