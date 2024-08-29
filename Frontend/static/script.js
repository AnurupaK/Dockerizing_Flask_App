document.addEventListener('DOMContentLoaded', async function () {
    const imageBtn = document.querySelector('.img')
    const imageInput = document.getElementById('imageInput')
    const input = document.querySelector('.input')
    const outputText = document.querySelector('.output_text')
    const outputImg = document.querySelector('.output_image')

    if (imageBtn) {
        console.log("Image button found")
        let currentInput = '';
        imageBtn.onclick = function () {
            imageInput.click();
        };

        imageInput.onchange = async function () {

            currentInput = imageInput.files[0];
            console.log("is it 1", currentInput instanceof File)
            console.log("Sending Image", currentInput)
            const imgElement = document.createElement('img');
            imgElement.src = URL.createObjectURL(currentInput); 
            console.log("Image url:", URL.createObjectURL(currentInput))
            imgElement.alt = "Uploaded Image";
            imgElement.style.maxWidth = '100%';
            imgElement.style.maxHeight = '400px';

            outputImg.appendChild(imgElement);

            let botImgRes = await getBotImgResponse(currentInput)
            console.log(botImgRes)
            outputText.innerHTML = botImgRes
        }
    }
    else {
        console.log("No image button found")
    }


    if(input){
        console.log("Input area found")
        input.addEventListener('keydown', async function(event){
           if (event.key === 'Enter'){
               event.preventDefault();
               console.log("Sending to server")
               inputmsg = input.value
               let msg = await getData(inputmsg)
               console.log(msg)
               outputText.innerHTML = msg
   
           }
        })
      }
      else{
        console.log("No output area found")
      }


})

async function getData(msg) {
     try{
         let response = await fetch('/api/text', {
             method: 'POST',
             headers: {
                 'Content-Type':'application/json'
             },
             body: JSON.stringify({msg:msg})
         })
 
         if(response.ok){
             let data = await response.json()
             return data.msg
 
         }
 
     }catch(error){
         console.log(error)
     }
     
 }

async function getBotImgResponse(imageFile) {
    const formData = new FormData();
    formData.append('file', imageFile);

    try {
        const response = await fetch('/api/image', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        return result.botImgResTxt;

    } catch (error) {
        console.error('Error during fetch:', error);
        throw error;
    }
}