import {AfterViewInit, Component, ViewChild} from '@angular/core';
import {MatTableDataSource} from "@angular/material/table";
import {MatSort} from "@angular/material/sort";
import {MatPaginator} from "@angular/material/paginator";
import {MessageService} from "../../common/services/message/message.service";



@Component({
  selector: 'app-page-registry',
  templateUrl: './page-registry.component.html',
  styleUrls: ['./page-registry.component.scss']
})
export class PageRegistryComponent implements AfterViewInit
{
    displayedColumns: string[] = [ "nickname", "email", "role" ];
    dataSource: MatTableDataSource<any> = new MatTableDataSource<any>();
    @ViewChild(MatSort) sort: MatSort;
    @ViewChild(MatPaginator) paginator: MatPaginator;


    constructor( private messageService: MessageService ) { }


    ngAfterViewInit(): void
    {
        this.messageService
            .get('users?order_by=nickname')
            .subscribe(retour => this.ngAfterViewInitCallback(retour), err => this.ngAfterViewInitCallback(err));
    }


    ngAfterViewInitCallback(retour: any): void
    {
        if(retour.status !== "success") {
            console.log(retour);
        }
        else {
            let tabPerson: { id: number, email: string, nickname: string, is_admin: boolean }[] = retour.data;
            tabPerson = tabPerson.map( person => {
                if(!person.is_admin) return Object.assign(person, {role: "utilisateur"});
                else return Object.assign(person, {role: "admin"});
            });
            this.dataSource = new MatTableDataSource(tabPerson);
            this.dataSource.sort = this.sort;
            this.dataSource.paginator = this.paginator;
        }
    }


    applyFilter(event: Event): void
    {
        const filterValue = (event.target as HTMLInputElement).value;
        this.dataSource.filter = filterValue.trim().toLowerCase();
    }

}
