import { Injectable } from '@angular/core';
import {Person} from "../../interfaces/Person";

@Injectable({
  providedIn: 'root'
})
export class FictitiousDatasService
{

    getUser(): Person
    {
        const id = (Math.floor(Math.random()*100000)).toString()
        return {
            id: id,
            login: "Riri"+id,
            email: "riri"+id+"@gmail.com",
            hashPass: "blablabla",
            role: "user",
        }
    }

    getAdmin(): Person
    {
        const id = (Math.floor(Math.random()*100000)).toString()
        return {
            id: id,
            login: "Fifi"+id,
            email: "fifi"+id+"@gmail.com",
            hashPass: "blablabla",
            role: "admin",
        }
    }

    getTabPerson(n: number): Person[]
    {
        let tab: Person[] = [];

        for(let i=0 ; i<n ; i++)
        {
            if(Math.random() < 0.5) tab.push(this.getUser());
            else tab.push(this.getAdmin());
        }

        return tab;
    }

}
