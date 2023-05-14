Feature: stock management
    As a admin 
    i want to manage stock inventory

    Scenario: Inventory adjusment
        Given User was login ("qa.rakamin.jubelio@gmail.com" and "Jubelio123!") and the user on the dahboard page
        When I click barang item and the list from dropdown menu will be shown
        And I click persediaan menu then persediaan page will shown
        And I click penyesuaian persediaan button 
        And i fill the keterangan
            and i select the lokasi
            and i select the name of product that i want to manage the stock 
        And i click simpan button
        Then the stock of product success to manage
        