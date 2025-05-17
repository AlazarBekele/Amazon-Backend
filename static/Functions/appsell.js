
    let Offdisplay = document.getElementById ('Second_discription_id')
    let Input_container = document.getElementById ('input_first')

    function Click_Next () {

        if (Input_container.textContent == "") {

            window.alert ('Fill the Blank')

        } if (Input_container.textContent != null) {

            Offdisplay.classList.remove ('Second_discription')
            Offdisplay.classList.add ('Off_display_class')

            Second_category_select.classList.remove ('Second_Category')
            Second_category_select.classList.add ('Popup')

        }

    }

    let Second_category_select = document.getElementById ('Second_Category_id')

    // function change_second () {

    //     if (Second_category_select)

    // }