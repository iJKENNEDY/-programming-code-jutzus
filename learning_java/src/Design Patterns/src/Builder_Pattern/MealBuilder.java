package Builder_Pattern;

public class MealBuilder 
{
	public Meal prepareVegMeal() {
		Meal meal = new Meal();
		meal.addItem(new B_VerBurger());
		meal.addItem(new CD_Coke());
		return meal;
	}
	
	public Meal prepareNonVegetal() {
		Meal meal = new Meal();
		meal.addItem(new B_ChikenBurger());
		meal.addItem(new CD_Pepsi());
		return meal;
	}
}
