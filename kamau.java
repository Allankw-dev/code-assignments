package com.example.webserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Service;
import jakarta.persistence.*;

import java.util.List;

@SpringBootApplication
public class WebServerApp {
    public static void main(String[] args) {
        SpringApplication.run(WebServerApp.class, args);
    }
}

@Entity
class WebServer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String type;
    private String location;
    private String url;

    public WebServer() {}
    public WebServer(String name, String type, String location, String url) {
        this.name = name;
        this.type = type;
        this.location = location;
        this.url = url;
    }

    // Getters & Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getUrl() { return url; }
    public void setUrl(String url) { this.url = url; }
}

interface WebServerRepository extends JpaRepository<WebServer, Long> {}

@Service
class WebServerService {
    @Autowired
    private WebServerRepository repository;

    public List<WebServer> getAllServers() {
        return repository.findAll();
    }

    public WebServer addServer(WebServer server) {
        return repository.save(server);
    }

    public WebServer updateServer(Long id, WebServer updatedServer) {
        return repository.findById(id).map(server -> {
            server.setName(updatedServer.getName());
            server.setType(updatedServer.getType());
            server.setLocation(updatedServer.getLocation());
            server.setUrl(updatedServer.getUrl());
            return repository.save(server);
        }).orElse(null);
    }

    public void deleteServer(Long id) {
        repository.deleteById(id);
    }
}

@RestController
@RequestMapping("/servers")
class WebServerController {
    @Autowired
    private WebServerService service;

    @GetMapping
    public List<WebServer> getAllServers() {
        return service.getAllServers();
    }

    @PostMapping
    public WebServer addServer(@RequestBody WebServer server) {
        return service.addServer(server);
    }

    @PutMapping("/{id}")
    public WebServer updateServer(@PathVariable Long id, @RequestBody WebServer server) {
        return service.updateServer(id, server);
    }

    @DeleteMapping("/{id}")
    public void deleteServer(@PathVariable Long id) {
        service.deleteServer(id);
    }
}