
<script>
import { onMount } from "svelte";

const API ="https://rickandmortyapi.com/api/character";
let data =[];
let characters=[];

onMount(async() => {
const res = await fetch(API);
data= await res.json();
characters = data.results;
});

</script>

//creamos nuestro estilos para la aplicacion
<style>
 .characters {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  }
  figure,
  img{
   width: 100%;
   margin: 0;
   }
   </style>

   // bloque-html
   <div class="characters">
    {#each characters as character}
    <figure>
    <img src={character.image} alt={character.name}/>
    <figcaption>{character.name}</figcaption>
    </figure>
    {:else}
    <p>loading...</p>
    {/each}
   </div>
