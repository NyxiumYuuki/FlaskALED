import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class FictitiousDatasService
{

    getUser()
    {
        const id = (Math.floor(Math.random()*100000)).toString()
        return {
            id: id,
            nickname: "Riri"+id,
            email: "riri"+id+"@gmail.com",
            hash_pass: "blablabla",
            is_admin: false,
        }
    }

    getAdmin()
    {
        const id = (Math.floor(Math.random()*100000)).toString()
        return {
            id: id,
            nickname: "Fifi"+id,
            email: "fifi"+id+"@gmail.com",
            hash_pass: "blablabla",
            is_admin: true,
        }
    }

    getTabPerson(n: number)
    {
        let tab = [];

        for(let i=0 ; i<n ; i++)
        {
            if(Math.random() < 0.5) tab.push(this.getUser());
            else tab.push(this.getAdmin());
        }

        return tab;
    }

}
