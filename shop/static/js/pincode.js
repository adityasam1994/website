// var country=document.getElementById('pc');
// function use(){
// var pc=country.value;
// if (country.value == 'IN'){
// jQuery('#mes').removeClass('hide');
// alert(pc);
// }

// }
// country.onchange=use;
// var mes=document.getElementById('#mes');
// mes.classList.remove('hide');


var GB=new RegExp(/^\d{3}-\d{4}/);
var G=new RegExp(/^[ABCD]{2}[1-9]{2}|[GHK]{1}/);
var GB1=new RegExp(/^[A-Z]{1}[0-9]{1}\s[0-9]{1}[A-Z]{2}$/);
var GB2=new RegExp(/^[A-Z]{1}[0-9]{2}\s[0-9]{1}[A-Z]{2}$/);
var GB3=new RegExp(/^[A-Z]{1}[0-9]{1}[A-Z]{1}\s[0-9]{1}[A-Z]{2}$/);
var GB4=new RegExp(/^[A-Z]{2}[0-9]{1}\s[0-9]{1}[A-Z]{2}$/);
var GB5=new RegExp(/^[A-Z]{2}[0-9]{2}\s[0-9]{1}[A-Z]{2}$/);
var GB6=new RegExp(/^[A-Z]{2}[0-9]{1}[A-Z]{1}\s[0-9]{1}[A-Z]{2}$/);



function check(){
var input=document.getElementById('pco').value;
var gb1test=GB1.test(input);
var gb2test=GB2.test(input);
var gb3test=GB3.test(input);
var gb4test=GB4.test(input);
var gb5test=GB5.test(input);
var gb6test=GB6.test(input);


if (gb1test == true){
    jQuery('#mes').addClass('hide');
}
else{
    if (gb2test == true){
        jQuery('#mes').addClass('hide');
    }
    else{
        if (gb3test == true){
            jQuery('#mes').addClass('hide');
        }
        else{
            if (gb4test == true){
                jQuery('#mes').addClass('hide');
            }
            else{
                if (gb5test == true){
                    jQuery('#mes').addClass('hide');
                }
                else{
                    if (gb6test == true){
                        jQuery('#mes').addClass('hide');
                    }
                    else{
                        jQuery('#mes').removeClass('hide');
                    }
                }
            }
        }
    }
}
}


function reset(){
    document.getElementById('pco').value="";
}

document.getElementById('pco').onblur=check;

document.onload=reset();


function check_small(){
    var input=document.getElementById('pco_small').value;
    var gb1test=GB1.test(input);
    var gb2test=GB2.test(input);
    var gb3test=GB3.test(input);
    var gb4test=GB4.test(input);
    var gb5test=GB5.test(input);
    var gb6test=GB6.test(input);
    
    
    if (gb1test == true){
        jQuery('#mes_small').addClass('hide');
    }
    else{
        if (gb2test == true){
            jQuery('#mes_small').addClass('hide');
        }
        else{
            if (gb3test == true){
                jQuery('#mes_small').addClass('hide');
            }
            else{
                if (gb4test == true){
                    jQuery('#mes_small').addClass('hide');
                }
                else{
                    if (gb5test == true){
                        jQuery('#mes_small').addClass('hide');
                    }
                    else{
                        if (gb6test == true){
                            jQuery('#mes_small').addClass('hide');
                        }
                        else{
                            jQuery('#mes_small').removeClass('hide');
                        }
                    }
                }
            }
        }
    }
    }
    
    
    function reset_small(){
        document.getElementById('pco_small').value="";
    }
    
    document.getElementById('pco_small').onblur=check_small;
    
    document.onload=resetsmall();