(define (problem nosliw-1-0)
(:domain nosliw)
(:objects
	 ai - hero
	 nosliw - dragon
	 sarorah - sorceress
	 whitebeard - wizard
	 bard - agent
	 pointy - sword
	 quill - pen
	 amulet - item
	 spellbook - item
	 talisman - item
	 ;d1 d2 d3 - diamond
	 happydale - town
	 blueforest - location
	 fortwood - location
	 mtkillemall - mountain
	 suntheatre - location
	 lakeoftheclouds - location
	 darkcave - cave

)

(:init (at ai happydale)
	(at sarorah blueforest)
	(at nosliw darkcave)
	(at bard suntheatre)
	(at whitebeard lakeoftheclouds)
	;(at d3 mtkillemall)
	;(different d1 d2)
	;(different d2 d3)
	;(different d1 d3)
	;(possesses ai d1)
	(possesses ai pointy)
	(possesses ai amulet)
	;(possesses bard d2)
	(possesses bard quill)
	(possesses sarorah spellbook)
	(possesses whitebeard talisman)
	(path-from-to happydale blueforest)
	(path-from-to happydale suntheatre)
	(path-from-to blueforest mtkillemall)
	(path-from-to blueforest fortwood)
	(path-from-to suntheatre lakeoftheclouds)
	(path-from-to fortwood happydale)
	(path-from-to lakeoftheclouds blueforest)
	(path-from-to lakeoftheclouds mtkillemall)
	(path-from-to mtkillemall fortwood)
	(path-from-to mtkillemall darkcave)
	(path-from-to darkcave lakeoftheclouds)
	

 )

(:goal (and 
	(possesses ai talisman)
	(possesses whitebeard spellbook)
	(possesses sarorah quill)
	(possesses bard amulet)
	))
)