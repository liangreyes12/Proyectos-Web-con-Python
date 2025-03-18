function marcarRealizada(tareaId) {
    fetch(`/realizar/${tareaId}`)
        .then(response => response.json())
        .then(data => {
            let tareaFila = document.getElementById(`tarea-${tareaId}`);
            let btn = document.getElementById(`btn-${tareaId}`);

            if (data.realizada) {
                tareaFila.classList.add("text-decoration-line-through", "text-muted");
                btn.classList.remove("btn-success");
                btn.classList.add("btn-secondary");
                btn.innerHTML = "✔";
            } else {
                tareaFila.classList.remove("text-decoration-line-through", "text-muted");
                btn.classList.remove("btn-secondary");
                btn.classList.add("btn-success");
                btn.innerHTML = "✖";
            }
        });
}