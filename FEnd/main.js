//animatia pentru text

$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn"
        },
        out: {
            effect: "bounceOut"
        }
    });
});


//text to speech
document.getElementById("askButton").addEventListener("click", async () => {
    const dropdown = document.getElementById("questionDropdown");
    const question = dropdown.options[dropdown.selectedIndex].text;
    const responseBox = document.getElementById("responseBox");
    const responseTextContainer = responseBox.querySelector(".tlt");

    if (question !== "Alege o întrebare!") {
        const response = await eel.get_response(question)();

        responseTextContainer.textContent = response;
        $(responseTextContainer).textillate({
            loop: false,
            in: {
                effect: "fadeInUp",
                delay: 50
            }
        });

        responseBox.style.display = "block";
    } else {

        responseTextContainer.textContent = "Te rog alege o întrebare mai întâi!";
        $(responseTextContainer).textillate({
            loop: false,
            in: {
                effect: "fadeInDown",
                delay: 50
            }
        });

        responseBox.style.display = "block";
    }
});

$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn"
        },
        out: {
            effect: "bounceOut"
        }
    });
});

document.getElementById("askButton").addEventListener("click", async () => {
    const dropdown = document.getElementById("questionDropdown");
    const question = dropdown.options[dropdown.selectedIndex].text;
    const responseBox = document.getElementById("responseBox");
    const responseTextContainer = responseBox.querySelector(".tlt");
    const useGPT = document.getElementById("useChatGPT").checked; //toggle pt chatgpt

    if (question !== "Alege o întrebare!") {
        let response;
        if (useGPT) {
            response = await eel.get_chatgpt_response(question)();
        } else {
            response = await eel.get_response(question)();
        }

        responseTextContainer.textContent = response;
        eel.speak_response(response)();

        $(responseTextContainer).textillate({
            loop: false,
            in: {
                effect: "fadeInUp",
                delay: 50
            }
        });

        responseBox.style.display = "block";
    } else {
        responseTextContainer.textContent = "Te rog alege o întrebare mai întâi!";
        eel.speak_response("Te rog alege o întrebare mai întâi!")();

        $(responseTextContainer).textillate({
            loop: false,
            in: {
                effect: "fadeInDown",
                delay: 50
            }
        });

        responseBox.style.display = "block";
    }
});