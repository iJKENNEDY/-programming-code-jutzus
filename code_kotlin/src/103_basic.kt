enum class Flour{
	WHEAT, CORN, CASSAVA
}

interface Exotic{
	func isExotic(): Boolean 
}

enum class Flour: Exotic{
	WHEAT {
		override fun isExotic(): Boolean{
			return false 
		}
	},

	CORN{
		override fun  isExotic(): Boolean{
			return false
		}
	},

	CASSAVA{
		override fun isExotic(): Boolean{
			return true 
		}
	}
}