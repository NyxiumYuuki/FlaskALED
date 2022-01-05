import {AfterViewInit, Component, ViewChild} from '@angular/core';
import {MatTableDataSource} from "@angular/material/table";
import {MatSort} from "@angular/material/sort";
import {MatPaginator} from "@angular/material/paginator";
import {FictitiousDatasService} from "../../common/services/fictitiousDatas/fictitious-datas.service";
import {MatDialog} from "@angular/material/dialog";



@Component({
  selector: 'app-page-registry',
  templateUrl: './page-registry.component.html',
  styleUrls: ['./page-registry.component.scss']
})
export class PageRegistryComponent implements AfterViewInit
{
    displayedColumns: string[] = [ "nickname", "email", "role" ];
    dataSource: MatTableDataSource<any>;
    @ViewChild(MatSort) sort: MatSort;
    @ViewChild(MatPaginator) paginator: MatPaginator;


    constructor( private fictitiousDatasService: FictitiousDatasService,
                 public dialog: MatDialog ) { }


    ngAfterViewInit(): void
    {
        // Faux code
        let tabPerson = this.fictitiousDatasService.getTabPerson(5);

        // Vrai code ...

        tabPerson = tabPerson.map( person => {
            if(!person.is_admin) return Object.assign(person, {role: "utilisateur"});
            else return Object.assign(person, {role: "admin"});
        });
        this.dataSource = new MatTableDataSource(tabPerson);
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
    }


    applyFilter(event: Event)
    {
        const filterValue = (event.target as HTMLInputElement).value;
        this.dataSource.filter = filterValue.trim().toLowerCase();
    }

}
