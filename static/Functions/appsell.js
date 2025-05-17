
    let Offdisplay = document.getElementById ('Off_dis')
    let Input_container = document.getElementById ('input_first')

    function Click_Next () {

        if (Input_container.textContent == "") {

            window.alert ('Fill the Blank')

        } if (Input_container.textContent != null) {

            Offdisplay.classList.remove ('Discritpion')
            Offdisplay.classList.add ('Off_display_class')

        }

    }