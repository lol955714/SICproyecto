function incrementar() {
valor = document.getElementById("cantidad");
valor.value++;
}
function decrementar() {
valor = document.getElementById("cantidad");
cond = document.getElementById("cebolla");
if (valor.value>=2)valor.value--;
if (cond.value>valor.value)cond.value=valor.value;
}
function incrementar1() {
total=document.getElementById("cantidad");
valor = document.getElementById("cebolla");
if(total.value>valor.value){
valor.value++;
}}
function decrementar1() {
valor = document.getElementById("cebolla");
if (valor.value>=1)
valor.value--;
}