Catmandont Pty Ltd is a camping gear store wishing to start up their online shopping system to attract more customers since online shopping is where most buyers shop now.

The following base definitions are as below:  
User: The person using the online shopping system. Essentially the customer.  
Shop: The owner of the online shopping system. They have admin control and is able to control what Items are for sale.  
Item: Something can be purchased on the online store.  
Discount: Something that can be added onto an Item so that its price is reduced  
LineItem: An Item with   
Cart: Comprises of 

The online shopping system will require the following:
- Items in the online store will have a name and a product description
- There are two type of Items sold in the online store, Clothing, and Camping
- Clothing will include size and colour
- Camping gear will include dimensions and weight
- Items can have Discounts attatched to them
- There are many different types of Discounts, include PercentageDiscount, FlatDiscount, BuyXGetOneFreeDiscount
- Discounts can be chained together *__recursively__*, with the most recently applied one added first
- PercentageDiscount reduces the current price (after any previously applied discount) by a percentage given
- FlatDiscount reduces the current price (after any previously applied discount) by a flat amount
- BuyXGetOneFree reduces the price of the next same item to $0 for every X Items bought. So for example, Buy 4 Get One Free means 4 Items are purchased at the current price, and the 5th of the same Item is free
- Shop can create an Item to make it available for purchase
- Shop can add a Discount to an Item
- Shop can remove the top level Discount (most recently added) off an Item
- Shop can remove an Item, effectively making it unavailble for purchase
- A User has a Cart, which can add LineItem
- A LineItem has reference to an Item available for purchase and the quantity to purchase
- A LineItem can calculate the base price, the discount, and the subtotal (the base price less the discount) for the single LineItem
-  A Cart can calculate the base price, the discount, and the subtotal (the base price less the discount) for the entire Cart
- A User can remove a LineItem out of their Cart
- A User can purchase their cart (and effectively emptying it)

Provide THREE (3) use cases which clearly show the features implemented in your UML diagram.