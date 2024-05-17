function redirect(x) 
{
    console.error('c')
    window.location.href = x;
    event.stopPropagation();
}