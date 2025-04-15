# cs-recycling-sort



Instructions
STEP 1
Recycle plastic
Sefa started a recycling service at his school. To help it succeed, he’s building an app where students can enter information about an item, and then the app tells them whether it belongs in the trash or in the recycling. Sefa wants to start the service by recycling plastic.

Add a conditional that sets waste_type to the value "recycling" if the item is plastic.
An item is plastic if the variable material contains the value "plastic". For all other materials, waste_type should contain "trash".

STEP 2
Trash small plastics
The app also asks for the length of the item in centimeters. Unfortunately, the recycling service cannot recycle small plastic items like bottle caps because they get caught in the recycling equipment.

Set waste_type to the value "trash" if a plastic item is smaller than 7.5 cm.
You'll need to add new conditional that compares against the length value. Remember that the order you check the conditions and update waste_type matters!

Large plastic items should go in the recycling, small plastic items should go in the trash, and all other items should go in the trash.
