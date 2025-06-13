
    let Offdisplay = document.getElementById ('Second_discription_id')
    let Input_container = document.getElementById ('input_first')
    let Step_icon = document.getElementById ('Step_icon2_id')

    function Click_Next () {

        if (Input_container.textContent != null) {

                Offdisplay.classList.remove ('Second_discription')
                Offdisplay.classList.add ('Off_display_class')
    
                Second_category_select.classList.remove ('Second_Category')
                Second_category_select.classList.add ('Popup')
    
                Step_icon.classList.add ('increase')
                Step_icon.classList.remove ('Step_icon2')

        }
    
    }

    let Second_category_select = document.getElementById ('Second_Category_id')

    // function change_second () {

    //     if (Second_category_select)

    // }